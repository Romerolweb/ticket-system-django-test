// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

/**
 * A simple API route handler.
 *
 * This handler responds to requests with a JSON object containing a name.
 * It's a sample API route provided by Next.js.
 *
 * @param {import('next').NextApiRequest} req - The request object.
 * @param {import('next').NextApiResponse} res - The response object.
 */
export default function handler(req, res) {
  res.status(200).json({ name: 'John Doe' })
}
