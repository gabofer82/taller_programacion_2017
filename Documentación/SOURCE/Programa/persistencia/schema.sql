CREATE TABLE "sucursales" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "domicilio" TEXT NOT NULL,
    "ubicacionGeoId" INTEGER NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "telefonos" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "numero" TEXT,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "telefonos_de_personas" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "telefonoId" INTEGER NOT NULL,
    "personaId" INTEGER NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "telefonos_de_sucursales" (
    "id" INTEGER PRIMARY KEY NOT NULL,
    "telefonoId" INTEGER NOT NULL,
    "sucursalId" INTEGER NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "ubicaciones_geograficas" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "ciudad" TEXT NOT NULL,
    "departamento" TEXT NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "documentos" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "tipo" TEXT NOT NULL CHECK(tipo = "cédula" or tipo = "pasaporte"),
    "numero" TEXT NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "persona" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "nombres" TEXT NOT NULL,
    "apellidos" TEXT NOT NULL,
    "domicilio" TEXT,
    "documentoId" INTEGER NOT NULL,
    "ubicacionGeoId" INTEGER NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "empleados" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "password" TEXT NOT NULL,
    "personaId" INTEGER NOT NULL,
    "sucursalId" INTEGER NOT NULL,
    "tipo" TEXT NOT NULL CHECK(tipo = 'administrativo' or tipo = 'laboratorista'),
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "pacientes" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "personaId" INTEGER NOT NULL,
    "activo" INTEGER NOT NULL DEFAULT (1),
    "penalizado" INTEGER NOT NULL DEFAULT (0),
    "fichaPacienteId" INTEGER NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "fichas_pacientes" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "reservaId" INTEGER NOT NULL,
    "analisisId" INTEGER NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "reservas_analisis" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "dia" TEXT NOT NULL,
    "hora" TEXT NOT NULL,
    "conformado" INTEGER NOT NULL DEFAULT (0),
    "numeroConforme" TEXT,
    "institucionMedId" INTEGER NOT NULL,
    "cupoId" INTEGER NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "analisis" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "fecha" TEXT NOT NULL,
    "reservaAnalisisId" INTEGER NOT NULL,
    "tipoAnalisisId" INTEGER NOT NULL,
    "laboratoristaId" INTEGER NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "instituciones_medicas" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "nombre" TEXT NOT NULL,
    "domicilio" TEXT,
    "telefonoId" INTEGER,
    "ubicacionGeoId" INTEGER,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "tipos_de_analisis" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "nombre" TEXT NOT NULL,
    "tercerizado" INTEGER NOT NULL DEFAULT (0),
    "precio" REAL DEFAULT (0),
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "tipos_de_analisis_de_laboratorio_externo" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "tipoDeAnalisis" INTEGER NOT NULL,
    "laboratorioExterno" INTEGER,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "tipo_de_analisis_de_sucursal" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "tipoDeAnalisisId" INTEGER NOT NULL,
    "sucursalId" INTEGER NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "agendas_diarias" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "dia" TEXT NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "cupos" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "hora" TEXT NOT NULL,
    "agendaDiariaId" INTEGER NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "cupos_por_tipos_de_analisis" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "cantidad" INTEGER NOT NULL DEFAULT (1),
    "cupoId" INTEGER NOT NULL,
    "tipoDeAnalisisId" INTEGER,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "laboratorios_externos" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "domicilio" TEXT NOT NULL,
    "ubicacionGeoId" INTEGER NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
CREATE TABLE "telefonos_de_labs_externos" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "laboratorioExtId" INTEGER NOT NULL,
    "telefonoId" INTEGER NOT NULL,
    "baja" INTEGER NOT NULL DEFAULT (0)
);
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Artigas', 'Artigas');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Canelones', 'Canelones');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Melo', 'Cerro Largo');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Colonia del Sacramento', 'Colonia');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Durazno', 'Durazno');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Trinidad', 'Flores');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Florida', 'Florida');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Minas', 'Lavalleja');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Maldonado', 'Maldonado');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Montevideo', 'Montevideo');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Paysandú', 'Paysandú');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Fray Bentos', 'Río Negro');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Rivera', 'Rivera');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Rocha', 'Rocha');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Salto', 'Salto');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('San José de Mayo', 'San José');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Mercedes', 'Soriano');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Tacuarembó', 'Tacuarembó');
INSERT INTO ubicaciones_geograficas (ciudad, departamento) VALUES ('Treinta y tres', 'Treinta y tres');
