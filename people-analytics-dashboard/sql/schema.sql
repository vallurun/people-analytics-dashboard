-- Example schema
CREATE TABLE hris (
  employee_id INT PRIMARY KEY,
  department TEXT,
  location TEXT,
  tenure_years FLOAT,
  performance_rating INT,
  salary INT,
  manager_tenure FLOAT,
  hire_date DATE,
  attrition INT
);

CREATE TABLE engagement (
  employee_id INT,
  eNPS INT,
  pulse_score INT
);

CREATE TABLE recruiting (
  employee_id INT,
  source TEXT,
  time_to_fill_days INT,
  diversity_flag INT
);
