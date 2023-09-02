package com.student.service;

import org.springframework.stereotype.Service;

import com.student.exception.StudentException;
import com.student.exception.UserException;
import com.student.model.Student;

@Service
public interface StudentService {
	
	public Student registerStudent(Student student, String key) throws StudentException, UserException;
	
	public Student getStudentById(Integer studentId) throws StudentException ;
	
	//public Student getStudentByName(String name) throws StudentException;

}
