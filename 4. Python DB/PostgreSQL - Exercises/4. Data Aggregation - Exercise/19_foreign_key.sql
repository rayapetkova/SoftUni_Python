CREATE TABLE employees_projects(
	id SERIAL PRIMARY KEY,
	employee_id INTEGER,
	project_id INTEGER,
	CONSTRAINT fk_employee_id
		FOREIGN KEY (employee_id)
		REFERENCES employees(id),
	CONSTRAINT fk_project_id
		FOREIGN KEY(project_id)
		REFERENCES projects(id)
);