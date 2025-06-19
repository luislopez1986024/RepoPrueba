Sistema Electoral - API de Votación
Un sistema RESTful para gestionar votantes, candidatos y votos, desarrollado en Python con Flask y SQL Server.

📌 Requisitos Técnicos
Python 3.13+
SQL Server (Local o remoto)

⚙️ Configuración
1. Instalar dependencias
   lo puede hacer desde el powershell de visual studio code y se instalan los siguientes paquetes:
A.Flask	2.3.2	Framework web para la API
B.pyodbc	4.0.39	Conexión con SQL Server
C.python-dotenv	1.0.0	Manejo de variables de entorno

Ejecuta el script SQL en database.sql para crear las tablas.

Configura la conexión en config.py (en mi caso utilizo seguridad integrada en SQL):
 DB_CONFIG = {
    'server': 'DESKTOP-BP8S587',  # Cambia por tu servidor
    'database': 'SistemaElectoral',
    'driver': 'ODBC Driver 17 for SQL Server',
    'trusted_connection': 'yes'  # Autenticación Windows
}

🚀 Endpoints
👥 Votantes
Método	Ruta	Descripción
POST	/api/v1/voters	Registrar un nuevo votante
GET	/api/v1/voters	Listar todos los votantes
GET	/api/v1/voters/{id}	Obtener un votante por ID
DELETE	/api/v1/voters/{id}	Eliminar un votante

Ejemplo de request con pos utilizando cURL:
curl -X POST http://localhost:5000/api/v1/voters -H "Content-Type: application/json" -d "{\"nombre\":\"Ana García\", \"email\":\"ana@example.com\"}"

🗳️ Votos
Método	Ruta	Descripción
POST	/api/v1/votes	Emitir un voto
GET	/api/v1/votes	Listar todos los votos
GET	/api/v1/votes/statistics	Estadísticas de votación
Ejemplo (cURL):
curl -X POST http://localhost:5000/api/v1/votes -H "Content-Type: application/json" -d "{\"votante_id\":1, \"candidato_id\":1}"

sistema_electoral/
├── app.py                  # Punto de entrada
├── config.py               # Configuración de la BD
├── requirements.txt        # Dependencias
│
├── Models/                 # Modelos de datos
│   ├── votante.py          # Lógica de votantes
│   ├── candidato.py        # Lógica de candidatos
│   └── voto.py             # Lógica de votos
│
├── Controllers/            # Reglas de negocio
│   ├── votantes_controller.py
│   ├── candidatos_controller.py
│   └── votos_controller.py
│
└── Views/                  # Endpoints API
    ├── votantes_view.py
    ├── candidatos_view.py
    └── votos_view.py



    🛠️ Ejecución
1.Inicia el servidor Flask:
 ejecutando la clase app.py

2. Se puede probar los endpoints con cURL, Postman o Insomnia.


POR ULTIMO , DEJO EL SCRIPT DE LA BASE DE DATOS DE SQL SERVER
SCRIPT:
USE [master]
GO
/****** Object:  Database [SistemaElectoral]    Script Date: 19/06/2025 12:58:04 ******/
CREATE DATABASE [SistemaElectoral]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'SistemaElectoral', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\SistemaElectoral.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'SistemaElectoral_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\SistemaElectoral_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [SistemaElectoral] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [SistemaElectoral].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [SistemaElectoral] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [SistemaElectoral] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [SistemaElectoral] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [SistemaElectoral] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [SistemaElectoral] SET ARITHABORT OFF 
GO
ALTER DATABASE [SistemaElectoral] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [SistemaElectoral] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [SistemaElectoral] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [SistemaElectoral] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [SistemaElectoral] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [SistemaElectoral] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [SistemaElectoral] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [SistemaElectoral] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [SistemaElectoral] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [SistemaElectoral] SET  ENABLE_BROKER 
GO
ALTER DATABASE [SistemaElectoral] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [SistemaElectoral] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [SistemaElectoral] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [SistemaElectoral] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [SistemaElectoral] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [SistemaElectoral] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [SistemaElectoral] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [SistemaElectoral] SET RECOVERY FULL 
GO
ALTER DATABASE [SistemaElectoral] SET  MULTI_USER 
GO
ALTER DATABASE [SistemaElectoral] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [SistemaElectoral] SET DB_CHAINING OFF 
GO
ALTER DATABASE [SistemaElectoral] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [SistemaElectoral] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [SistemaElectoral] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [SistemaElectoral] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'SistemaElectoral', N'ON'
GO
ALTER DATABASE [SistemaElectoral] SET QUERY_STORE = OFF
GO
USE [SistemaElectoral]
GO
/****** Object:  Table [dbo].[Candidatos]    Script Date: 19/06/2025 12:58:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Candidatos](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [nvarchar](100) NOT NULL,
	[partido] [nvarchar](100) NULL,
	[votos] [int] NOT NULL,
	[es_votante] [bit] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Votantes]    Script Date: 19/06/2025 12:58:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Votantes](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [nvarchar](100) NOT NULL,
	[email] [nvarchar](100) NOT NULL,
	[ha_votado] [bit] NOT NULL,
	[es_candidato] [bit] NOT NULL,
	[creado_en] [datetime] NULL,
	[actualizado_en] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[email] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Votos]    Script Date: 19/06/2025 12:58:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Votos](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[votante_id] [int] NOT NULL,
	[candidato_id] [int] NOT NULL,
	[timestamp] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [UQ_Voto_Votante] UNIQUE NONCLUSTERED 
(
	[votante_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Index [IX_Candidatos_Votos]    Script Date: 19/06/2025 12:58:04 ******/
CREATE NONCLUSTERED INDEX [IX_Candidatos_Votos] ON [dbo].[Candidatos]
(
	[votos] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [IX_Votantes_HaVotado]    Script Date: 19/06/2025 12:58:04 ******/
CREATE NONCLUSTERED INDEX [IX_Votantes_HaVotado] ON [dbo].[Votantes]
(
	[ha_votado] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Candidatos] ADD  DEFAULT ((0)) FOR [votos]
GO
ALTER TABLE [dbo].[Candidatos] ADD  DEFAULT ((0)) FOR [es_votante]
GO
ALTER TABLE [dbo].[Votantes] ADD  DEFAULT ((0)) FOR [ha_votado]
GO
ALTER TABLE [dbo].[Votantes] ADD  DEFAULT ((0)) FOR [es_candidato]
GO
ALTER TABLE [dbo].[Votantes] ADD  DEFAULT (getdate()) FOR [creado_en]
GO
ALTER TABLE [dbo].[Votantes] ADD  DEFAULT (getdate()) FOR [actualizado_en]
GO
ALTER TABLE [dbo].[Votos] ADD  DEFAULT (getdate()) FOR [timestamp]
GO
ALTER TABLE [dbo].[Votos]  WITH CHECK ADD FOREIGN KEY([candidato_id])
REFERENCES [dbo].[Candidatos] ([id])
GO
ALTER TABLE [dbo].[Votos]  WITH CHECK ADD FOREIGN KEY([votante_id])
REFERENCES [dbo].[Votantes] ([id])
GO
USE [master]
GO
ALTER DATABASE [SistemaElectoral] SET  READ_WRITE 
GO
