package com.student.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.student.exception.StudentException;
import com.student.exception.UserException;
import com.student.model.Student;
import com.student.service.StudentService;

import jakarta.validation.Valid;

@RestController
public class StudentController {
	
	@Autowired
    private StudentService sService;

    @PostMapping("/students")
    public ResponseEntity<Student> addStudent(@Valid @RequestBody Student student, @RequestParam(required = false)
    String key) throws StudentException, UserException {
        return new ResponseEntity<Student>(sService.registerStudent(student, key), HttpStatus.CREATED);

    }
    
    @GetMapping("/students/{studentId}")
    public ResponseEntity<Student> viewStudentbyId(@PathVariable("studentId") Integer Id) throws StudentException{
        return new ResponseEntity<Student>(sService.getStudentById(Id), HttpStatus.ACCEPTED);
//		http://localhost:8888/students/studentId
    }

}
