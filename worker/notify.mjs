export function emailText(record, chain) {
  const { fields } = record;
  return [
    `Project: ${fields.project}`,
    `Website: ${fields.website}`,
    `Category: ${fields.category}`,
    `Chains: ${fields.chains || "-"}`,
    `Twitter: ${fields.twitter || "-"}`,
    `Contact email: ${fields.email}`,
    `Telegram: ${fields.telegram || "-"}`,
    "",
    "Description:",
    fields.description,
    "",
    "Notes:",
    fields.notes || "-",
    "",
    `Paid: ${record.amountDisplay} ${record.token} on ${chain.name}`,
    `From: ${record.from}`,
    `Transaction: ${chain.explorer}${record.txHash}`,
    `Received: ${record.createdAt}`,
  ].join("\n");
}

export async function sendEmail(record, chain, env) {
  const { MJ_APIKEY_PUBLIC, MJ_APIKEY_PRIVATE, LISTING_EMAIL_FROM, LISTING_EMAIL_TO } = env;
  if (!MJ_APIKEY_PUBLIC || !MJ_APIKEY_PRIVATE || !LISTING_EMAIL_FROM || !LISTING_EMAIL_TO) {
    throw new Error("Mailjet environment is not configured");
  }
  const response = await fetch("https://api.mailjet.com/v3.1/send", {
    method: "POST",
    headers: {
      "content-type": "application/json",
      authorization: "Basic " + btoa(`${MJ_APIKEY_PUBLIC}:${MJ_APIKEY_PRIVATE}`),
    },
    body: JSON.stringify({
      Messages: [
        {
          From: { Email: LISTING_EMAIL_FROM, Name: "defiprime listings" },
          To: [{ Email: LISTING_EMAIL_TO }],
          Subject: `Paid listing: ${record.fields.project}`,
          TextPart: emailText(record, chain),
        },
      ],
    }),
  });
  if (!response.ok) throw new Error(`Mailjet answered ${response.status}`);
}
