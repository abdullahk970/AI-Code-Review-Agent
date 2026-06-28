interface Props {
  riskScore: number;
  decision: string;
}

export default function RiskBadge({ riskScore, decision }: Props) {
  const getRiskColor = (score: number) => {
    if (score <= 20) return "bg-green-100 text-green-800 border-green-200";
    if (score <= 50) return "bg-yellow-100 text-yellow-800 border-yellow-200";
    if (score <= 80) return "bg-orange-100 text-orange-800 border-orange-200";
    return "bg-red-100 text-red-800 border-red-200";
  };

  const getRiskLabel = (score: number) => {
    if (score <= 20) return "Low Risk";
    if (score <= 50) return "Medium Risk";
    if (score <= 80) return "High Risk";
    return "Critical";
  };

  return (
    <div className="flex items-center space-x-2">
      <div
        className={`px-3 py-1 rounded-full text-sm font-semibold border ${getRiskColor(
          riskScore
        )}`}
      >
        {getRiskLabel(riskScore)} ({riskScore})
      </div>
      <span
        className={`text-sm font-medium ${
          decision === "APPROVE"
            ? "text-green-600"
            : decision === "MINOR_FIXES"
              ? "text-yellow-600"
              : "text-red-600"
        }`}
      >
        {decision}
      </span>
    </div>
  );
}
