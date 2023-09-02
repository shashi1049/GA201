package com.student.serviceImpl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.student.exception.UserException;
import com.student.model.CurrentUserSession;
import com.student.model.User;
import com.student.repository.CurrentUserSessionRepo;
import com.student.repository.UserRepo;
import com.student.service.IUserService;



@Service
public class IUserServiceImpl implements IUserService{
	
	@Autowired
	private UserRepo uRepo;
	
	@Autowired
	private CurrentUserSessionRepo srepo;
	
	@Override
	public User addUser(User user) throws UserException {
		User u= uRepo.findByEmail(user.getEmail());
		
		if(u!=null) {
			throw new UserException("User already exist with this username.");
		}
		
		return uRepo.save(user);
	}
	

	@Override
	public User updateUser(User user,String key) throws UserException {
		CurrentUserSession loggedInUser=srepo.findByUuid(key);
		
		if(loggedInUser==null) {
			throw new UserException("Please provide a valid key to update user");
		}
		
		User curr=uRepo.findById(user.getUserLoginId())
				.orElseThrow(()-> new UserException("User with User Id "+user.getUserLoginId()+" does not exist"));
		
		if (loggedInUser.getUserType().equals("STUDENT")) {
		
			
			
			if (user.getEmail() != null) curr.setEmail(user.getEmail());
			
			if (user.getName() != null) curr.setName(user.getName());
			
			
			
			if (user.getPassword() != null) curr.setPassword(user.getPassword());
			

			
			User saved = uRepo.save(curr);
			
			return saved;
		}
		
		
		if(user.getEmail().equals(curr.getEmail())) {
		
			
			
			if (user.getEmail() != null) curr.setEmail(user.getEmail());
			
			if (user.getName() != null) curr.setName(user.getName());
			
			
			
			if (user.getPassword() != null) curr.setPassword(user.getPassword());
			

			
			User saved = uRepo.save(curr);
			
			return saved;
			
		}
		
		else throw new UserException("Access denied.");
				
	}

	@Override
	public User deleteUser(String key) throws UserException {
		
		CurrentUserSession loggedInUser=srepo.findByUuid(key);
		
		if(loggedInUser==null) {
		
			throw new UserException("Please provide a valid key to delete user.");
		}

		User user = uRepo.findByEmail(loggedInUser.getEmail());

		if(user != null){

			uRepo.delete(user);
			srepo.delete(loggedInUser);

			return user;

		}else {
			throw new UserException("User not found with this email");
		}



		
	}

	@Override
	public User viewUser(String key) throws UserException {
		
		CurrentUserSession loggedInUser=srepo.findByUuid(key);
		
		if(loggedInUser==null) {
			throw new UserException("Please first login to view user details.");
		}

		User user = uRepo.findByEmail(loggedInUser.getEmail());

		if(user == null){

			throw new UserException("User not found");
		}

		return user;

	}

	
	
	@Override
	public List<User> viewAllUsers(String key) throws UserException {
		
		CurrentUserSession loggedInUser=srepo.findByUuid(key);
		
		if(loggedInUser==null) {
			
			throw new UserException("Please provide a valid key to find all user.");
		}
		
		if (loggedInUser.getUserType().name().equals("ADMIN")) {
			
			List<User> users=uRepo.findAll();
			
			if(users.size()!=0) {
				return users;
			}
			
			else {
				throw new UserException("No User Found.");
			}
		}
		
		else throw new UserException("Access denied");
	}

}
