import json

diccionario={}

jerarquia_unisangil= {"nombre": "Unisangil",
                      "rector": {
                      "nombre":"Patricia Lequerica Moreno",
                      "cargo":"Rector"
    
},
"facultades":[
    {
    "nombre":"facultad de derecho",
    "decano":{
        "nombre": "pepito",
        "cargo": "decano"
    },
    "programas":
        {
        "nombre":"Derecho",
        "director": {
            "nombre": "juan",
            "cargo": "Director de programa"
        }
        },
    
    "nombre2":{
        "bnombre":"Facultad de ciencias economicas y administrativas",
        "decano":{
        "nombre2.":"pedro",
        "cargo": "Decano"
        },
        "programas":[
        {
            "nombre":"Administracion de empresas",
            "director":{
            "nombred":"pablo",
            "cargo.":"Director de programa"
            },
            "nombrec":{
            "nombrec.":"Contaduria Publica",
            "directorr":{
                "nombre.s":"carlos",
                "cargo..":"Director de programa"
            }
            }
        }
        ]
    },
    "nombre3":{
        "Nombre":"Facultad de ciencias naturales e ingenieria",
        "decano3":{
        "Nombre":"juanita",
        "cargo":"Decano"
        },
        "programas":[
        {
            "nombre":"Tecnologia en sistemas de informacion",
            "director":{
            "Nombre3":"Noc",
            "Cargo":"Director de programa"
            },
            "nombrei":{
            "NNombre":"Ingenieria de sistemas",
            "Director":{
                "Nombree":"Nelson Santos",
                "Cargo..":"Director de programa"
            },
            "Semestres":[
                {
                "noms1":"Primer semestre"
                },
                {
                "noms2":"Segundo semestre"
                },
                {
                "noms3":"Tercer semestre"
                },
                {
                "noms4":"Cuarto Semestre"
                },
                {
                "noms5":"Quinto semestre" ,
                "materias":[
                    {
                    "nombrem1":"Administracion y gestion de bases de datos",
                    "docente":"Edisson Caicedo"
                    },
                    {
                    "nombrem2":"Proyecto Integrador",
"docente":"Ivan Velazques"
                    },
                    {
                    "nombrem3":"Expresion 2",
                    "Docente.":"Adriana Mayorga"
                    },
                    {
                    "nombrem4":"Biologia General",
                    "Docent":"Ivan Velasques"
                    },
                    {
                    "nombrem5":"Ondas y Particulas",
                    "Docente..":"Carlos Cortes"
                    },
                    {
                    "nombrem6.":"Analisis de Algoritmos",
                    "DOcente":"Jesus David Garcia Caro",
                    "Correo":"jdgarcia1@unisangil.edu.co",
                    "Descripcion":"En esta clase vera los coinjuntos de operaciones que permiten dar solucion a un problema"
                    }
                ]
                }
                
            
            ]
            
            }
        }
        ]
        
    }
    
    
    }
]
}

print(unisangil)