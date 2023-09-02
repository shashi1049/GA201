package com.student.repository;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import com.student.model.Student;

@Repository
public interface StudentRepo extends JpaRepository<Student, Integer>{
	
	@Query("from Student s where s.name LIKE %:name% ") 
	public List<Student> getStudentsByName(String name) ;

	
	
}
