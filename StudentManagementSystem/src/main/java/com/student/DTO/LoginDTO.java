package com.student.DTO;

import com.student.model.UserType;

import jakarta.validation.constraints.NotNull;
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
	
	@NotNull(message ="User cannot be null.")
	private UserType userType;
	
	
	
}
