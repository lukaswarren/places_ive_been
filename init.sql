CREATE TABLE IF NOT EXISTS places (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    country VARCHAR(100),
    visit_date date, -- Assuming month/year format (e.g., "01/2023")
    visit_number INT,
    length_of_stay INT,
    pictureGroupingId INT UNIQUE,
    blog_entry INT
);

-- Create the pictures table
CREATE TABLE IF NOT EXISTS pictures (
    id SERIAL PRIMARY KEY,
    pictureid VARCHAR(100),  -- Adjust data type and length as needed
    picture_grouping_id INT,
    FOREIGN KEY (picture_grouping_id) REFERENCES places (pictureGroupingId)
);

-- Seed data for places table
INSERT INTO places (city, country, visit_date, visit_number, length_of_stay, pictureGroupingId) VALUES
    ('New York', 'USA', '2023-01-01', 1, 5, 1),
    ('Paris', 'France', '2023-05-01', 2, 3, 2),
    ('Tokyo', 'Japan', '2023-09-01', 3, 7, 3);



