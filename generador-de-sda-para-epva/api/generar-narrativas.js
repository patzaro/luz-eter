export async function POST(req) {
  const body = await req.json();

  const prompt = `
Eres un experto en pedagogía visual. Dado el saber básico "${body.topic}" para el curso "${body.course}", y el contexto "${body.context}", genera tres posibles narrativas educativas inspiradoras.
`;

  const res = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=TU_CLAVE', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      contents: [{ parts: [{ text: prompt }] }]
    })
  });

  const data = await res.json();

  // suponiendo que Gemini devuelve texto con las tres narrativas separadas
  const texto = data.candidates?.[0]?.content?.parts?.[0]?.text || '';
  const narrativas = texto.split('\n').filter(Boolean);

  return new Response(JSON.stringify({ narrativas }));
}
