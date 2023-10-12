DELETE from volunteers_departments
WHERE department_name = (SELECT department_name FROM volunteers_departments WHERE department_name = 'Education program assistant')
