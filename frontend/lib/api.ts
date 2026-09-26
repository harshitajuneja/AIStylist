export interface StylistRequest {
  destination?: string;
  occasion?: string;
  body_type?: string;
  undertone?: string;
  style?: string;
  budget_min?: number;
  budget_max?: number;
  query?: string;
}

export async function getRecommendations(
  data: StylistRequest
) {

  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/recommend`,
    {
      method: "POST",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify(data)
    }
  );

  if (!response.ok) {
    throw new Error(
      "Failed to fetch recommendations"
    );
  }

  return response.json();
}