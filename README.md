# AI Voice Agent by Jannis Moore

This AI Voice Agent is designed and built by Jannis Moore to provide an advanced telephony interface using Vocode's telephony server. For more information and other projects by Jannis Moore, visit [Integraticus](https://integraticus.com) and check out the [YouTube Channel](https://www.youtube.com/@jannismoore/featured).

## Setup Manual

To set up the AI Voice Agent, follow these steps:

1. Sign up to [Render.com](https://render.com).
2. Navigate to "New" > "Web Service" and connect your GitHub account if you haven't done that yet.
3. Fork and import [this repository](https://github.com/jannismoore/ai-voice-agent-vocode-template) within Render.com.
4. Once done, Render will automatically set most of the values for you. You can customize the Region as you wish.
5. Set the following environment variables: 
    - `OPENAI_API_KEY`: Set this to your OpenAI API key.
    - `TRANSCRIPT_CALLBACK_URL`: Set this to the URL you want to call once a call was completed.
    - `TWILIO_ACCOUNT_SID`: Your Twilio Account ID.
    - `TWILIO_AUTH_TOKEN`: Your Twilio Auth token.
    - `DEEPGRAM_API_KEY`: The API key for your Deepgram Acccount.
6. Once the app is deployed successfully, copy the Render.com URL and add `/inbound_call` at the end of it
7. Paste that URL into the Webhook field of your Twilio Phone Number

## Manual Installation

This part of the manual is intended if you run the installation locally.

First, build the application using Docker:

```docker build -t jannismoore-telephony-app .```

Then, run the application using docker-compose. From the `telephony_app` directory, run:

```docker-compose up```


## Vocode Self-hosted Telephony Server

For a more detailed guide on setting up the telephony server, visit [Vocode's official documentation](https://docs.vocode.dev/open-source/telephony).

See [Vocode's Self-hosted Telephony Setup](https://docs.vocode.dev/telephony#self-hosted) for detailed setup steps!
