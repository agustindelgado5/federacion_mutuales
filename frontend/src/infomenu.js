
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
            children: [
                {
                    title: `Prueba 1`,
                    children: [
                        {
                            title: `Prueba 1.1`,
                            link: `/`,
                            children: [],
                        },
                        {
                            title: `Prueba 1.2`,
                            link: `/`,
                            children: [],
                        },
                        {
                            title: `Prueba 1.3`,
                            link: `/`,
                            children: [],
                        },
                    ],
                },
            ],
         
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
                    link: '/ordenesmedicas',
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
                    link: `/profesionales`,
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
