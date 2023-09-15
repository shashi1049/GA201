package com.student.model;

import java.time.LocalDateTime;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
public class CurrentUserSession {
	
	// current user
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer currentId;
    private String email;
    private String uuid;
    private LocalDateTime localDateTime;
    private UserType userType;

    

    public CurrentUserSession(String email, String uuid, LocalDateTime localDateTime, UserType userType) {
        this.email = email;
        this.uuid = uuid;
        this.localDateTime = localDateTime;
        this.userType = userType;
    }

    
}
