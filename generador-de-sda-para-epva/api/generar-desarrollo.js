export async function POST(req) {
  const body = await req.json();

  const prompt = `
Dado el curso "${body.curso}", la narrativa educativa: "${body.narrativa}", y ${body.sesiones} sesiones previstas, genera una Situación de Aprendizaje completa que incluya:

1. Título sugerido
2. Competencias específicas implicadas
3. Saber básico abordado
4. Actividades principales
5. Criterios de evaluación
6. Indicadores de logro
7. Recursos y materiales
8. Vinculación con el currículo gallego (LOMLOE)

Presenta el desarrollo como un texto claro y bien organizado, sin formato Markdown, y sin emoticonos.
`;

  const res = await fetch(
    'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=TU_API_KEY',
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ parts: [{ text: prompt }] }]
      })
    }
  );

  const data = await res.json();
  const desarrollo = data.candidates?.[0]?.content?.parts?.[0]?.text || '';

  return new Response(
    JSON.stringify({ desarrollo }),
    { headers: { 'Content-Type': 'application/json' } }
  );
}
