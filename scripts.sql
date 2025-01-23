-- Tabela de clientes
CREATE TABLE client (
    client_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    address TEXT,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP)
);

-- Tabela de funcionários
CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    role TEXT CHECK (role IN ('mechanic', 'manager', 'admin')) DEFAULT 'mechanic',
    hired_date DATE NOT NULL,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP)
);

-- Tabela de veículos
CREATE TABLE vehicle (
    vehicle_id INTEGER PRIMARY KEY,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    license_plate TEXT UNIQUE NOT NULL,
    client_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP),
    FOREIGN KEY (client_id) REFERENCES client(client_id)
);

-- Tabela de trabalhos realizados
CREATE TABLE work (
    work_id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    cost REAL NOT NULL,
    status TEXT CHECK (status IN ('pending', 'in_progress', 'completed', 'canceled')) DEFAULT 'pending',
    vehicle_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicle(vehicle_id)
);

-- Tabela de tarefas atribuídas
CREATE TABLE task (
    task_id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    employee_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status TEXT NOT NULL DEFAULT 'pending',
    work_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP),
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
    FOREIGN KEY (work_id) REFERENCES work(work_id)
);

-- Tabela de faturas
CREATE TABLE invoice (
    invoice_id INTEGER PRIMARY KEY,
    client_id INTEGER NOT NULL,
    issued_at DATETIME NOT NULL,
    total REAL NOT NULL,
    iva REAL NOT NULL,
    total_with_iva REAL NOT NULL,
    FOREIGN KEY (client_id) REFERENCES client(client_id)
);

-- Tabela de itens de fatura
CREATE TABLE invoice_item (
    item_id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    cost REAL NOT NULL,
    invoice_id INTEGER NOT NULL,
    task_id INTEGER,
    FOREIGN KEY (invoice_id) REFERENCES invoice(invoice_id),
    FOREIGN KEY (task_id) REFERENCES task(task_id)
);

-- Tabela de configurações globais
CREATE TABLE setting (
    setting_id INTEGER PRIMARY KEY,
    key_name TEXT NOT NULL UNIQUE,
    value TEXT NOT NULL,
    updated_at DATETIME DEFAULT (CURRENT_TIMESTAMP)
);


-- Inserir dados na tabela de clientes
INSERT INTO client (name, email, phone, address) VALUES
('João Silva', 'joao.silva@example.com', '912345678', 'Rua A, 123, Lisboa'),
('Maria Oliveira', 'maria.oliveira@example.com', '913456789', 'Av. B, 456, Porto'),
('Carlos Santos', 'carlos.santos@example.com', '914567890', 'Rua C, 789, Faro'),
('Ana Pereira', 'ana.pereira@example.com', '915678901', 'Rua D, 321, Coimbra'),
('Ricardo Gonçalves', 'ricardo.goncalves@example.com', '916789012', 'Av. E, 654, Braga');


-- Inserir dados na tabela de funcionários
INSERT INTO employee (name, email, phone, role, hired_date) VALUES
('Rui Ferreira', 'rui.ferreira@example.com', '910123456', 'mechanic', '2023-01-15'),
('Ana Costa', 'ana.costa@example.com', '911234567', 'manager', '2022-06-10'),
('Pedro Martins', 'pedro.martins@example.com', '912345678', 'mechanic', '2024-02-20'),
('Tiago Almeida', 'tiago.almeida@example.com', '913456789', 'mechanic', '2024-03-10'),
('Sofia Lopes', 'sofia.lopes@example.com', '914567890', 'admin', '2021-11-01');

-- Inserir dados na tabela de veículos
INSERT INTO vehicle (brand, model, year, license_plate, client_id) VALUES
('Toyota', 'Corolla', 2015, 'AA-12-BB', 1),
('Ford', 'Focus', 2018, 'CC-34-DD', 2),
('Honda', 'Civic', 2020, 'EE-56-FF', 3),
('Volkswagen', 'Golf', 2017, 'GG-78-HH', 4),
('Nissan', 'Qashqai', 2019, 'II-90-JJ', 5);

-- Inserir dados na tabela de trabalhos (works)
INSERT INTO work (description, cost, status, vehicle_id, start_date, end_date) VALUES
('Troca de óleo', 50.00, 'completed', 1, '2023-08-01', '2023-08-01'),
('Revisão completa', 200.00, 'in_progress', 2, '2023-08-10', NULL),
('Substituição de pastilhas de travão', 80.00, 'pending', 3, NULL, NULL),
('Inspeção do motor', 150.00, 'completed', 4, '2023-07-15', '2023-07-16'),
('Reparação de suspensão', 300.00, 'canceled', 5, '2023-06-20', '2023-06-21');

-- Inserir dados na tabela de tarefas
INSERT INTO task (description, employee_id, start_date, end_date, status, work_id) VALUES
('Reparação do motor', 1, '2023-07-01', '2023-07-03', 'completed', 1),
('Troca de bateria', 2, '2023-07-15', NULL, 'in_progress', 2),
('Alinhamento de direção', 3, '2023-08-01', '2023-08-02', 'completed', 3);

-- Inserir dados na tabela de faturas
INSERT INTO invoice (client_id, issued_at, total, iva, total_with_iva) VALUES
(1, '2023-08-10 14:30:00', 100.00, 23.00, 123.00),
(2, '2023-08-15 10:00:00', 200.00, 46.00, 246.00);

-- Inserir dados na tabela de itens de fatura
INSERT INTO invoice_item (description, cost, invoice_id, task_id) VALUES
('Troca de óleo', 50.00, 1, 1),
('Substituição de travões', 80.00, 2, 2);

-- Inserir dados na tabela de configurações
INSERT INTO setting (key_name, value) VALUES
('IVA_PERCENT', '23'),
('GARAGE_NAME', 'Garage XPTO');