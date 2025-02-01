-- Crear la base de datos si no existe
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'GestionEventos')
BEGIN
    CREATE DATABASE GestionEventos;
END;
GO

USE GestionEventos;
GO

-- Eliminar la tabla si ya existe para evitar duplicados
IF OBJECT_ID('Eventos', 'U') IS NOT NULL
BEGIN
    DROP TABLE Eventos;
END;
GO

-- Crear la tabla Eventos con los campos tipo y categoría
CREATE TABLE Eventos (
    id_evento INT PRIMARY KEY IDENTITY(1,1),
    categoria NVARCHAR(50),  -- 🔹 Se agregó la categoría del evento
    tipo NVARCHAR(50),       -- 🔹 Se agregó el tipo de evento
    nombre NVARCHAR(100),
    fecha DATE,
    ubicacion NVARCHAR(255)
);
GO

-- Crear el procedimiento almacenado para insertar eventos
IF OBJECT_ID('InsertarEvento', 'P') IS NOT NULL
BEGIN
    DROP PROCEDURE InsertarEvento;
END;
GO

CREATE PROCEDURE InsertarEvento
    @categoria NVARCHAR(50), -- 🔹 Se agregó la categoría en el procedimiento almacenado
    @tipo NVARCHAR(50),      -- 🔹 Se agregó el tipo de evento
    @nombre NVARCHAR(100),
    @fecha DATE,
    @ubicacion NVARCHAR(255)
AS
BEGIN
    INSERT INTO Eventos (categoria, tipo, nombre, fecha, ubicacion)
    VALUES (@categoria, @tipo, @nombre, @fecha, @ubicacion);

    PRINT 'Evento insertado exitosamente';
END;
GO

-- Eliminar los registros previos antes de insertar nuevos eventos
DELETE FROM Eventos;
GO

-- Insertar eventos usando el procedimiento almacenado
EXEC InsertarEvento 'social', 'boda', 'Boda de Ana', '2025-03-15', 'Quito';
EXEC InsertarEvento 'social', 'cumpleaños', 'Cumpleaños de Pedro', '2025-02-10', 'Guayaquil';
EXEC InsertarEvento 'social', 'graduación', 'Graduación de Carla', '2025-06-20', 'Cuenca';
EXEC InsertarEvento 'academico', 'conferencia', 'Conferencia de Tecnología', '2025-04-10', 'Quito';
EXEC InsertarEvento 'academico', 'seminario', 'Seminario de Innovación', '2025-05-22', 'Guayaquil';
EXEC InsertarEvento 'deportivo', 'maratón', 'Maratón Quito 10K', '2025-07-12', 'Quito';
EXEC InsertarEvento 'deportivo', 'torneo', 'Torneo de Fútbol Intercolegial', '2025-08-18', 'Cuenca';
GO

-- Verificar los datos insertados
SELECT * FROM Eventos;
GO
