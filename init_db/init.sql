USE nombres;

CREATE TABLE IF NOT EXISTS nombres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO nombres (nombre) VALUES ('Anibal');
INSERT INTO nombres (nombre) VALUES ('Jordan');