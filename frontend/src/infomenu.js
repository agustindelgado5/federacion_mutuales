
const data = {
    title: 'Federacion de Mutuales',
    children: [
        {
            title: `Inicio`,
            link: `/`,
            children: [],
        },
        {
            title: `Usuarios`,
            link: `/usuarios`,
            children: [],
        },
        {
            title: `Socios`,
            link: '/socios',
            children: [],
        },
        {
            title: `Profesionales`,
            link: '/profesionales',
            children: [],
        },
        {
            title: `Cobradores`,
            link: '/cobradores',
            children: [],
        },
        {
            title: `Salud`,
            link: '/salud',
            children: [
                {
                    title: `Ordenes Medicas`,
                    link: '/ordenes',
                    children: [],
                },
                {
                    title: `Institutos`,
                    link: '/institutos',
                    children: [],
                },
                {
                    title: `Estudios`,
                    link: '/estudios',
                    children: [
                        {
                            title: `Imagenes`,
                            link: `/`,
                            children: [],
                        },
                        {
                            title: `Analisis Bioquimicos`,
                            link: `/`,
                            children: [],
                        },
                    ],
                },
                {
                    title: `Cirugias`,
                    link: '/cirugias',
                    children: [],
                },
            ],

        },
        {
            title: `Farmacias`,
            link: '/farmacias',
            children: [
                {
                    title: `Info Farmacias`,
                    link: `/farmacias`,
                    children: [],
                },
                {
                    title: `Medicamentos`,
                    link: `/medicamentos`,
                    children: [],
                },
                {
                    title: `Recetas`,
                    link: `/recetas`,
                    children: [],
                },
            ],
        },
        {
            title: `Registro Contable`,
            link: '/registrocontable',
            children: [
                {
                    title: `Gastos Salientes`,
                    link: `/salientes`,
                    children: [],
                },
                {
                    title: `Gastos Profesionales`,
                    link: `/profesionales/list_pagos`,
                    children: [],
                },
                {
                    title: `Cuotas de Socios`,
                    link: `/cuotas`,
                    children: [],
                },
            ],
        },
        {
            title: `Mutuales`,
            link: '/mutuales',
            children: [],
        },
        {
            title: `Servicios`,
            link: '/servicios',
            children: [],
        },
    ],
};

export default data;
