-- Create the 'caller' table
CREATE TABLE caller (
                        caller_id INT PRIMARY KEY,
                        name VARCHAR(255),
                        department VARCHAR(255),
                        contact_info VARCHAR(255)
);

-- Create the 'equipment' table
CREATE TABLE equipment (
                           equipment_id INT PRIMARY KEY,
                           type VARCHAR(50),
                           make VARCHAR(50),
                           model VARCHAR(50)
);

-- Create the 'specialist' table
CREATE TABLE specialist (
                            specialist_id INT PRIMARY KEY,
                            name VARCHAR(255),
                            expertise_area VARCHAR(255)
);

-- Create the 'problem' table with foreign keys to 'caller', 'equipment', and 'specialist'
CREATE TABLE problem (
                         problem_id INT PRIMARY KEY,
                         description TEXT,
                         status VARCHAR(50),
                         caller_id INT,
                         equipment_id INT,
                         specialist_id INT,
                         FOREIGN KEY (caller_id) REFERENCES caller(caller_id),
                         FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id),
                         FOREIGN KEY (specialist_id) REFERENCES specialist(specialist_id)
);
