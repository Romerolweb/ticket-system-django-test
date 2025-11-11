import { Html, Head, Main, NextScript } from 'next/document'

/**
 * A custom Document component for Next.js.
 *
 * This component is used to customize the server-rendered HTML document,
 * allowing for modifications to the `<html>` and `<body>` tags.
 *
 * @returns {JSX.Element} The rendered Document component.
 */
export default function Document() {
  return (
    <Html lang="en">
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
