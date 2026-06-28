interface Props {
  total_reviews: number;
  approvals: number;
  change_requests: number;
}

export default function StatsCards({
  total_reviews,
  approvals,
  change_requests,
}: Props) {
  const stats = [
    {
      title: "Total Reviews",
      value: total_reviews,
      icon: "📊",
      color: "from-blue-500 to-blue-600",
      bgColor: "bg-blue-50",
      textColor: "text-blue-600",
    },
    {
      title: "Approvals",
      value: approvals,
      icon: "✅",
      color: "from-green-500 to-green-600",
      bgColor: "bg-green-50",
      textColor: "text-green-600",
    },
    {
      title: "Change Requests",
      value: change_requests,
      icon: "⚠️",
      color: "from-orange-500 to-orange-600",
      bgColor: "bg-orange-50",
      textColor: "text-orange-600",
    },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      {stats.map((stat) => (
        <div
          key={stat.title}
          className={`${stat.bgColor} rounded-lg p-6 border border-gray-200 hover:shadow-lg transition-shadow`}
        >
          <div className="flex items-start justify-between">
            <div>
              <p className={`text-sm font-medium ${stat.textColor}`}>
                {stat.title}
              </p>
              <p className={`text-4xl font-bold ${stat.textColor} mt-2`}>
                {stat.value}
              </p>
            </div>
            <div className="text-3xl">{stat.icon}</div>
          </div>
          <div className={`mt-4 h-1 w-full bg-gradient-to-r ${stat.color} rounded`} />
        </div>
      ))}
    </div>
  );
}
