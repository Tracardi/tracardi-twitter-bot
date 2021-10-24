from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result
from tracardi_twitter_bot.model.model import Config, TwitterCredentials
from tracardi_twitter_bot.service.twitter_client import TwitterClient
from tracardi.service.storage.driver import storage


class TwitterBotActions(ActionRunner):

    @staticmethod
    async def build(**kwargs) -> 'TwitterBotActions':
        config = Config(**kwargs)
        source = await storage.driver.resource.load(config.source.id)
        data = TwitterCredentials(**source.config)

        return TwitterBotActions(config, data)

    def __init__(self, config: Config, resource_credentials: TwitterCredentials):
        self.config = config
        self.client = TwitterClient(resource_credentials)

    async def run(self, payload):
        if self.config.action == 'mention':
            await self.client.like_all_mentions()
        elif self.config.action == 'follow':
            await self.client.auto_follow_followers()
        return Result(port="payload", value=payload)


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_twitter_bot.plugin',
            className='TwitterBotActions',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Risto Kowaczewski",
            init={
                'source': {
                    'id': None
                },
                "action": None
            }),
        metadata=MetaData(
            name='Tweet auto actions',
            desc='This plugin is performs auto likes of mentions and auto following followers.',
            type='flowNode',
            width=200,
            height=100,
            icon='twitter',
            group=["Connectors"]
        )
    )
