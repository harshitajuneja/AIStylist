"use client";

import { useState } from "react";
import { getRecommendations } from "@/lib/api";

interface Props {
  onResults: (data: any[]) => void;
}

export default function StylistForm({
  onResults
}: Props) {

  const [destination, setDestination] =
    useState("bali");

  const [occasion, setOccasion] =
    useState("sunset_dinner");

  const [bodyType, setBodyType] =
    useState("pear");

  const [undertone, setUndertone] =
    useState("warm");

  const [style, setStyle] =
    useState("tropical_glam");

  const [budget, setBudget] =
    useState("50000");

  const [query, setQuery] =
    useState("");

  const [loading, setLoading] =
    useState(false);


  async function handleSubmit(
    e: React.FormEvent
  ) {

    e.preventDefault();

    setLoading(true);

    try {

      const data =
        await getRecommendations({

          destination,

          occasion,

          body_type: bodyType,

          undertone,

          style,

          budget_max:
            Number(budget),

          query

        });

      onResults(
        data.recommendations
      );

    } catch (error) {

      console.error(error);

      alert(
        "Unable to get recommendations"
      );

    } finally {

      setLoading(false);

    }
  }


  return (

    <form
      onSubmit={handleSubmit}
      className="space-y-6"
    >

      <div>

        <label>
          Where are you going?
        </label>

        <select
          value={destination}
          onChange={(e) =>
            setDestination(e.target.value)
          }
        >

          <option value="bali">
            Bali
          </option>

          <option value="maldives">
            Maldives
          </option>

          <option value="santorini">
            Santorini
          </option>

          <option value="goa">
            Goa
          </option>

        </select>

      </div>


      <div>

        <label>
          Occasion
        </label>

        <select
          value={occasion}
          onChange={(e) =>
            setOccasion(e.target.value)
          }
        >

          <option value="sunset_dinner">
            Sunset Dinner
          </option>

          <option value="luxury_brunch">
            Luxury Brunch
          </option>

          <option value="pool_party">
            Pool Party
          </option>

          <option value="yacht">
            Yacht
          </option>

          <option value="honeymoon">
            Honeymoon
          </option>

        </select>

      </div>


      <div>

        <label>
          Body Type
        </label>

        <select
          value={bodyType}
          onChange={(e) =>
            setBodyType(e.target.value)
          }
        >

          <option value="hourglass">
            Hourglass
          </option>

          <option value="pear">
            Pear
          </option>

          <option value="apple">
            Apple
          </option>

          <option value="rectangle">
            Rectangle
          </option>

          <option value="inverted_triangle">
            Inverted Triangle
          </option>

        </select>

      </div>


      <div>

        <label>
          Undertone
        </label>

        <select
          value={undertone}
          onChange={(e) =>
            setUndertone(e.target.value)
          }
        >

          <option value="warm">
            Warm
          </option>

          <option value="cool">
            Cool
          </option>

          <option value="neutral">
            Neutral
          </option>

        </select>

      </div>


      <div>

        <label>
          Style
        </label>

        <select
          value={style}
          onChange={(e) =>
            setStyle(e.target.value)
          }
        >

          <option value="tropical_glam">
            Tropical Glam
          </option>

          <option value="quiet_luxury">
            Quiet Luxury
          </option>

          <option value="boho_luxe">
            Boho Luxe
          </option>

          <option value="coastal_chic">
            Coastal Chic
          </option>

          <option value="romantic_feminine">
            Romantic Feminine
          </option>

        </select>

      </div>


      <div>

        <label>
          Budget
        </label>

        <input
          type="number"
          value={budget}
          onChange={(e) =>
            setBudget(e.target.value)
          }
        />

      </div>


      <div>

        <label>
          Tell your stylist anything else
        </label>

        <textarea
          value={query}
          onChange={(e) =>
            setQuery(e.target.value)
          }
          placeholder="I want something elegant and flowy..."
        />

      </div>


      <button
        type="submit"
        disabled={loading}
      >

        {loading
          ? "Creating your looks..."
          : "Create My Resort Look ✦"}

      </button>

    </form>

  );
}