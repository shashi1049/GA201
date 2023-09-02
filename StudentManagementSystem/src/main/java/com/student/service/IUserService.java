package com.student.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.student.exception.UserException;
import com.student.model.User;


@Service
public interface IUserService {
	
	//Methods of user
	public User addUser(User user) throws UserException;
	
	public User updateUser(User user,String key) throws UserException;
	
	public User deleteUser(String key) throws UserException;
	
	public User viewUser(String key) throws UserException;
	
	public List<User> viewAllUsers(String key) throws UserException;
}