package com.example.userservice.service;

import com.example.userservice.model.User;
import com.example.userservice.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class UserService {
    
    private final UserRepository userRepository;
    
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }
    
    public Optional<User> getUserById(String id) {
        return userRepository.findById(id);
    }
    
    public Optional<User> getUserByUsername(String username) {
        return userRepository.findByUsername(username);
    }
    
    public Optional<User> getUserByEmail(String email) {
        return userRepository.findByEmail(email);
    }
    
    public User createUser(User user) {
        // Check if username or email already exists
        if (userRepository.existsByUsername(user.getUsername())) {
            throw new IllegalArgumentException("Username already exists");
        }
        
        if (userRepository.existsByEmail(user.getEmail())) {
            throw new IllegalArgumentException("Email already exists");
        }
        
        // Set creation and update timestamps
        LocalDateTime now = LocalDateTime.now();
        user.setCreatedAt(now);
        user.setUpdatedAt(now);
        
        return userRepository.save(user);
    }
    
    public Optional<User> updateUser(String id, User userDetails) {
        return userRepository.findById(id)
                .map(existingUser -> {
                    // Check if username is being changed and if it already exists
                    if (!existingUser.getUsername().equals(userDetails.getUsername()) &&
                            userRepository.existsByUsername(userDetails.getUsername())) {
                        throw new IllegalArgumentException("Username already exists");
                    }
                    
                    // Check if email is being changed and if it already exists
                    if (!existingUser.getEmail().equals(userDetails.getEmail()) &&
                            userRepository.existsByEmail(userDetails.getEmail())) {
                        throw new IllegalArgumentException("Email already exists");
                    }
                    
                    // Update fields
                    existingUser.setUsername(userDetails.getUsername());
                    existingUser.setEmail(userDetails.getEmail());
                    existingUser.setFirstName(userDetails.getFirstName());
                    existingUser.setLastName(userDetails.getLastName());
                    existingUser.setActive(userDetails.isActive());
                    existingUser.setUpdatedAt(LocalDateTime.now());
                    
                    return userRepository.save(existingUser);
                });
    }
    
    public boolean deleteUser(String id) {
        return userRepository.findById(id)
                .map(user -> {
                    userRepository.delete(user);
                    return true;
                })
                .orElse(false);
    }
}
