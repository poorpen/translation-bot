import logging
import asyncio

from src.presentation.telegram import setup_config, parametrize_bot

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.info("starting bot")
    config = setup_config()
    bot, dp = parametrize_bot(config)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
