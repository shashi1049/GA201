package com.student.service;

import org.springframework.stereotype.Service;

import com.student.DTO.LoginDTO;
import com.student.exception.LoginException;
import com.student.model.CurrentUserSession;

@Service
public interface LoginService {
	
	//login and logout methods 
	public CurrentUserSession logIntoAccount(LoginDTO dto) throws LoginException;
	
	public String logOutFromAccount(String key) throws LoginException;
}
