"use client";

import { useState } from "react";

import StylistForm
  from "@/components/StylistForm";

import RecommendationCard
  from "@/components/RecommendationCard";


export default function Home() {

  const [results, setResults] =
    useState<any[]>([]);


  return (

    <main className="min-h-screen bg-[#f7f3ef]">

      <section className="mx-auto max-w-7xl px-6 py-16">

        <div className="grid gap-12 lg:grid-cols-2">

          {/* LEFT */}

          <div>

            <p className="text-sm uppercase tracking-[0.3em]">
              The Vision
            </p>

            <h1 className="mt-5 text-6xl font-serif">
              Your Personal
              <br />
              AI Stylist
            </h1>

            <p className="mt-6 max-w-xl text-lg text-gray-600">

              Discover resort looks curated around
              your destination, occasion, proportions,
              undertone and personal aesthetic.

            </p>


            <div className="mt-10 rounded-3xl bg-white p-8 shadow-sm">

              <StylistForm
                onResults={setResults}
              />

            </div>

          </div>


          {/* RIGHT */}

          <div>

            {results.length === 0 ? (

              <div className="flex min-h-105 items-center justify-center rounded-3xl bg-[#e9dfd7]">

                <div className="max-w-sm text-center">

                  <p className="text-5xl">
                    ✦
                  </p>

                  <h2 className="mt-5 text-3xl font-serif">

                    Let's create
                    your look.

                  </h2>

                  <p className="mt-4 text-gray-600">

                    Tell your stylist where you're
                    going and what kind of experience
                    you want to create.

                  </p>

                </div>

              </div>

            ) : (

              <div className="space-y-8">

                <div>

                  <p className="text-sm uppercase tracking-[0.25em]">
                    Your Curated Edit
                  </p>

                  <h2 className="mt-2 text-4xl font-serif">
                    Looks selected for you
                  </h2>

                </div>


                {results.map(
                  (item, index) => (

                    <RecommendationCard
                      key={index}
                      recommendation={item}
                    />

                  )
                )}

              </div>

            )}

          </div>

        </div>

      </section>

    </main>

  );
}