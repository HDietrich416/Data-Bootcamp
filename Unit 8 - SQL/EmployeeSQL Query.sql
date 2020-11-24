--Data Analysis:

-- 1. List the following details of each employee: employee number, last name, first name, sex, and salary.

SELECT employees.emp_no, last_name, first_name, sex, salary
FROM employees
JOIN salaries on salaries.emp_no = employees.emp_no;


-- 2. List first name, last name, and hire date for employees who were hired in 1986.

SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date LIKE '%1986';

-- 3. List the manager of each department with the following information: 
--department number, department name, the manager's employee number, last name, first name.

SELECT dept_manager.dept_no, departments.dept_name, dept_manager.emp_no, last_name, first_name
FROM dept_manager
JOIN departments ON departments.dept_no = dept_manager.dept_no
JOIN employees ON employees.emp_no = dept_manager.emp_no;

-- 4. List the department of each employee with the following information: 
--employee number, last name, first name, and department name.

SELECT employees.emp_no, last_name, first_name, departments.dept_name
FROM employees
JOIN dept_emp ON dept_emp.emp_no = employees.emp_no
JOIN departments ON departments.dept_no = dept_emp.dept_no;


-- 5. List first name, last name, and sex for employees whose first 
-- name is "Hercules" and last names begin with "B."

SELECT first_name, last_name, sex
FROM employees
WHERE first_name = 'Hercules'
AND last_name LIKE 'B%';

--6. List all employees in the Sales department, including their employee number, 
--last name, first name, and department name.

CREATE VIEW Sales_emp_names AS
	SELECT emp_no, last_name, first_name
	FROM employees
	WHERE emp_no IN (
				SELECT emp_no
				FROM dept_emp
				WHERE dept_no = (
							SELECT dept_no
							FROM departments
							WHERE dept_name = 'Sales'))
	ORDER BY emp_no ASC;


CREATE VIEW Sales_emp_dept AS
	SELECT emp_no, departments.dept_name
	FROM dept_emp
	JOIN departments ON departments.dept_no = dept_emp.dept_no
	WHERE dept_emp.dept_no  = (
				SELECT dept_no
				FROM departments
				WHERE dept_name = 'Sales')
	ORDER BY emp_no ASC;

SELECT Sales_emp_names.emp_no, Sales_emp_names.last_name, Sales_emp_names.first_name, Sales_emp_dept.dept_name
FROM sales_emp_names
JOIN Sales_emp_dept ON Sales_emp_dept.emp_no = sales_emp_names.emp_no;

--7.List all employees in the Sales and Development departments, including their 
--employee number, last name, first name, and department name.

CREATE VIEW sales_dev_emp_names AS
	SELECT emp_no, last_name, first_name
	FROM employees
	WHERE emp_no IN (
				SELECT emp_no
				FROM dept_emp
				WHERE dept_no IN (
							SELECT dept_no
							FROM departments
							WHERE dept_name = 'Sales'
							OR dept_name = 'Development'));
		
CREATE VIEW sales_dev_emp_dept AS	
	SELECT emp_no, departments.dept_name
	FROM dept_emp
	JOIN departments ON departments.dept_no = dept_emp.dept_no
	WHERE dept_emp.dept_no IN (
				SELECT dept_no
				FROM departments
				WHERE dept_name = 'Sales'
				OR dept_name = 'Development')
			
SELECT sales_dev_emp_names.emp_no, sales_dev_emp_names.last_name, sales_dev_emp_names.first_name, sales_dev_emp_dept.dept_name
FROM sales_dev_emp_names
JOIN sales_dev_emp_dept ON sales_dev_emp_dept.emp_no = sales_dev_emp_names.emp_no;

--8. In descending order, list the frequency count of employee last names, 
--i.e., how many employees share each last name.

SELECT last_name, COUNT(last_name)
FROM employees
GROUP BY last_name
ORDER BY COUNT(last_name) DESC