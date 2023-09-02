package com.student.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.student.model.CurrentUserSession;

@Repository
public interface CurrentUserSessionRepo extends JpaRepository<CurrentUserSession, Integer> {
	
	// finding current user using uuid and email
    public CurrentUserSession findByUuid(String Uuid);

    public CurrentUserSession findByEmail(String email);



}
