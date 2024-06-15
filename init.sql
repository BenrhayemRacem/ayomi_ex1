-- Create schema if not exists
CREATE SCHEMA IF NOT EXISTS public;

-- Set default schema search path to public
SET search_path TO public;

-- Create tables

-- Table: operation

CREATE TABLE IF NOT EXISTS public.operation (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    expression TEXT,
    result TEXT,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
);

-- Table: Step

CREATE TABLE public.step (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    index INTEGER,
    execution TEXT,
    operation_id INTEGER NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    FOREIGN KEY (operation_id) REFERENCES public.operation(id)
);

