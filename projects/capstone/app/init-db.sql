CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO tasks (title, description) VALUES
('CI/CD Pipeline Initialized', 'Automated GitHub Actions build passed successfully.'),
('Infrastructure Provisioned', 'Terraform deployed VPC, Subnets, and EC2 application instances.');
