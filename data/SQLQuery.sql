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

-- Crear la tabla Eventos con el campo tipo
CREATE TABLE Eventos (
    id_evento INT PRIMARY KEY IDENTITY(1,1),
    tipo NVARCHAR(50),  -- 🔹 Se agregó el campo tipo
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
    @tipo NVARCHAR(50),  -- 🔹 Se agregó el tipo en el procedimiento almacenado
    @nombre NVARCHAR(100),
    @fecha DATE,
    @ubicacion NVARCHAR(255)
AS
BEGIN
    INSERT INTO Eventos (tipo, nombre, fecha, ubicacion)
    VALUES (@tipo, @nombre, @fecha, @ubicacion);

    PRINT 'Evento insertado exitosamente';
END;
GO

-- Eliminar los registros previos antes de insertar nuevos eventos
DELETE FROM Eventos;
GO

-- Insertar eventos usando el procedimiento almacenado
EXEC InsertarEvento 'boda', 'Boda de Ana', '2025-03-15', 'Quito';
EXEC InsertarEvento 'cumpleaños', 'Cumpleaños de Pedro', '2025-02-10', 'Guayaquil';
EXEC InsertarEvento 'graduación', 'Graduación de Carla', '2025-06-20', 'Cuenca';
GO

-- Verificar los datos insertados
SELECT * FROM Eventos;
GO
