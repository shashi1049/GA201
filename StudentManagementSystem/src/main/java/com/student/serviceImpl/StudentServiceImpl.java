package com.student.serviceImpl;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.student.exception.StudentException;
import com.student.exception.UserException;
import com.student.model.CurrentUserSession;
import com.student.model.Student;
import com.student.repository.CourseRepo;
import com.student.repository.CurrentUserSessionRepo;
import com.student.repository.StudentRepo;
import com.student.service.StudentService;

@Service
public class StudentServiceImpl implements StudentService{
	
	@Autowired
	private StudentRepo srepo;
	
	@Autowired
	private CourseRepo corepo;
	
	@Autowired
    private CurrentUserSessionRepo crepo;

	@Override
	public Student registerStudent(Student student, String key) throws StudentException, UserException {
		// TODO Auto-generated method stub
		CurrentUserSession currentUserSession = crepo.findByUuid(key);

        if(currentUserSession == null){
            throw new UserException("Admin Not logged in");
        }
        if(currentUserSession.getUserType().name().equals("ADMIN")){
        	return srepo.save(student);
        }
        else{
            throw new UserException("Plz log in as Admin");

        }
	}

	@Override
	public Student getStudentById(Integer studentId) throws StudentException {
		Optional<Student> opt = srepo.findById(studentId);
        if(opt.isPresent()) {
            Student student = opt.get();
            return student;
        }
        else {
            throw new StudentException("No Bus present with given id : "+studentId);
        }
	}

	

}
