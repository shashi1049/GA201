package com.student.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.student.exception.UserException;
import com.student.model.User;
import com.student.service.IUserService;

import jakarta.validation.Valid;



@RestController
public class UserController {
	
	@Autowired
	private IUserService uService;

	@PostMapping("/add")
	public ResponseEntity<User> addUserHandler(@Valid @RequestBody User user) throws UserException {
		User u=uService.addUser(user);
		return new ResponseEntity<User>(u,HttpStatus.CREATED);
	}
	
	@PutMapping("/update")
	public ResponseEntity<User> updateUserHandler(@Valid @RequestBody User user,@RequestParam String key) throws UserException {
		User u=uService.updateUser(user,key);
		return new ResponseEntity<User>(u,HttpStatus.ACCEPTED);
	}
	
	@DeleteMapping("delete")
	public ResponseEntity<User> deleteUserHandler(@RequestParam String key) throws UserException {
		User u=uService.deleteUser( key);
		return new ResponseEntity<User>(u,HttpStatus.ACCEPTED);
	}
	
	@GetMapping("/view")
	public ResponseEntity<User> viewUserHandler(@RequestParam String key) throws UserException {
		User u=uService.viewUser(key);
		return new ResponseEntity<User>(u,HttpStatus.FOUND);
	}
	
	@GetMapping("/viewall")
	public ResponseEntity<List<User>> viewAllUsersHandler(@RequestParam String key) throws UserException {
		List<User> users=uService.viewAllUsers(key);
		return new ResponseEntity<List<User>>(users,HttpStatus.FOUND);
	}
}
