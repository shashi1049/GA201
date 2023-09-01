package com.example.demo.model;

import java.util.HashSet;
import java.util.Set;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToMany;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;

@Entity
@Data  // @Getter and @Setter
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode
public class Course {



	
	
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private Integer courseId;
	private String courseName;
	private Integer fee;
	private String desc;
	
	
	@ManyToMany(cascade = CascadeType.ALL, mappedBy = "courses")
	private Set<Student> students= new HashSet<>();

		
}
