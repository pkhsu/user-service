import streamlit as st
st.set_page_config(page_title="用戶管理系統", layout="wide")  # 移到這裡

from pymongo import MongoClient
from datetime import datetime
import time

# MongoDB 連接設定 (使用docker容器名稱)
MONGO_URI = "mongodb://root:password@mongodb:27017/"
DB_NAME = "user-service"
COLLECTION_NAME = "users"

# 初始化 MongoDB 連接
@st.cache_resource
def init_connection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db[COLLECTION_NAME]

collection = init_connection()

# 顯示用戶列表
def display_users():
    st.header("用戶列表")
    users = list(collection.find())
    
    if not users:
        st.info("沒有找到任何用戶")
        return
    
    for user in users:
        with st.expander(f"{user['firstName']} {user['lastName']} ({user['username']})"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Email:** {user['email']}")
                st.write(f"**創建時間:** {user['createdAt'].strftime('%Y-%m-%d %H:%M')}")
                st.write(f"**狀態:** {'啟用' if user['active'] else '停用'}")
            with col2:
                if st.button("編輯", key=f"edit_{user['_id']}"):
                    st.session_state.edit_user = user
                if st.button("刪除", key=f"delete_{user['_id']}"):
                    collection.delete_one({"_id": user["_id"]})
                    st.success("用戶已刪除")
                    time.sleep(1)
                    st.rerun()
                if st.button("切換狀態", key=f"toggle_{user['_id']}"):
                    collection.update_one(
                        {"_id": user["_id"]},
                        {"$set": {"active": not user["active"], "updatedAt": datetime.now()}}
                    )
                    st.success(f"用戶已{'啟用' if not user['active'] else '停用'}")
                    time.sleep(1)
                    st.rerun()

# 新增/編輯用戶表單
def user_form():
    st.header("新增/編輯用戶")
    
    if 'edit_user' in st.session_state:
        user = st.session_state.edit_user
        is_edit = True
    else:
        user = {
            "username": "",
            "email": "",
            "firstName": "",
            "lastName": "",
            "active": True
        }
        is_edit = False
    
    with st.form(key="user_form"):
        username = st.text_input("用戶名*", value=user["username"])
        email = st.text_input("Email*", value=user["email"])
        firstName = st.text_input("名字*", value=user["firstName"])
        lastName = st.text_input("姓氏*", value=user["lastName"])
        active = st.checkbox("啟用", value=user["active"])
        
        submitted = st.form_submit_button("儲存")
        
        if submitted:
            if not all([username, email, firstName, lastName]):
                st.error("請填寫所有必填欄位(*)")
            else:
                user_data = {
                    "username": username,
                    "email": email,
                    "firstName": firstName,
                    "lastName": lastName,
                    "active": active,
                    "updatedAt": datetime.now()
                }
                
                if is_edit:
                    user_data["createdAt"] = user["createdAt"]
                    collection.update_one({"_id": user["_id"]}, {"$set": user_data})
                    st.success("用戶已更新")
                    del st.session_state.edit_user
                else:
                    user_data["createdAt"] = datetime.now()
                    collection.insert_one(user_data)
                    st.success("用戶已新增")
                
                time.sleep(1)
                st.rerun()

# 主程式
def main():
    st.title("用戶管理系統")
    
    tab1, tab2 = st.tabs(["用戶列表", "新增用戶"])
    
    with tab1:
        display_users()
    
    with tab2:
        user_form()

if __name__ == "__main__":
    main()
