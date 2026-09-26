interface Props {
  recommendation: any;
}

export default function RecommendationCard({
  recommendation
}: Props) {

  const product =
    recommendation.product;

  return (

    <div className="overflow-hidden rounded-2xl bg-white shadow">

      <img
        src={product.image_url}
        alt={product.name}
        className="h-105 w-full object-cover"
      />

      <div className="p-6">

        <p className="text-sm uppercase tracking-[0.2em] text-gray-500">
          Curated for you
        </p>

        <h3 className="mt-2 text-2xl font-serif">
          {product.name}
        </h3>

        <p className="mt-2 text-gray-600">
          {product.description}
        </p>

        <div className="mt-4 flex flex-wrap gap-2">

          <span className="rounded-full bg-gray-100 px-3 py-1 text-sm">
            {product.silhouette}
          </span>

          <span className="rounded-full bg-gray-100 px-3 py-1 text-sm">
            {product.neckline}
          </span>

          <span className="rounded-full bg-gray-100 px-3 py-1 text-sm">
            {product.pattern}
          </span>

        </div>


        <div className="mt-6">

          <h4 className="font-medium">
            Why this look?
          </h4>

          <ul className="mt-2 space-y-1 text-sm text-gray-600">

            {recommendation.reasons?.map(
              (reason: string, index: number) => (

                <li key={index}>
                  ✦ {reason}
                </li>

              )
            )}

          </ul>

        </div>

        <p className="mt-6 text-lg font-medium">

          ₹{Number(product.price).toLocaleString("en-IN")}

        </p>

      </div>

    </div>

  );
}