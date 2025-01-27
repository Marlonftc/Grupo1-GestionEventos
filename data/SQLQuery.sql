-- Crear la base de datos
CREATE DATABASE GestionEventos;
GO

USE GestionEventos;
GO
 
-- Crear la tabla Eventos
CREATE TABLE Eventos (
    id_evento INT PRIMARY KEY IDENTITY(1,1),
    nombre NVARCHAR(100),
    fecha DATE,
    ubicacion NVARCHAR(255)
);
GO
 
-- Crear el procedimiento almacenado para insertar eventos
CREATE PROCEDURE InsertarEvento
    @nombre NVARCHAR(100),
    @fecha DATE,
    @ubicacion NVARCHAR(255)
AS
BEGIN
    INSERT INTO Eventos (nombre, fecha, ubicacion)
    VALUES (@nombre, @fecha, @ubicacion);
 
    PRINT 'Evento insertado exitosamente';
END;
GO
 
-- Insertar eventos usando el procedimiento almacenado
EXEC InsertarEvento 'Boda de Ana', '2025-03-15', 'Quito';
EXEC InsertarEvento 'Cumpleaños de Pedro', '2025-02-10', 'Guayaquil';
GO
 
-- Verificar los datos insertados
SELECT * FROM Eventos;
GO