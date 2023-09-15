package com.student.DTO;

import javax.validation.constraints.NotNull;

import com.student.model.UserType;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class LoginDTO {
	
	@NotNull(message ="Email cannot be null.")
	private String email;
	
	@NotNull(message ="Password cannot be null.")
	private String password;
	
	private UserType userType;
	
	
	
}
