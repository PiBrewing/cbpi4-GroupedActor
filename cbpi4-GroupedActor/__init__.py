
# -*- coding: utf-8 -*-
import os
from aiohttp import web
import logging
from unittest.mock import MagicMock, patch
import asyncio
import random
from cbpi.api import *
from cbpi.api.base import CBPiBase

logger = logging.getLogger(__name__)


@parameters([Property.Actor(label="Actor01", description="Select an actor to be controlled by this group."),
            Property.Actor(label="Actor02", description="Select an actor to be controlled by this group."),
            Property.Actor(label="Actor03", description="Select an actor to be controlled by this group."),
            Property.Actor(label="Actor04", description="Select an actor to be controlled by this group."),
            Property.Actor(label="Actor05", description="Select an actor to be controlled by this group."),
            Property.Actor(label="Actor06", description="Select an actor to be controlled by this group."),
            Property.Actor(label="Actor07", description="Select an actor to be controlled by this group."),
            Property.Actor(label="Actor08", description="Select an actor to be controlled by this group.")])

class CustomActor(CBPiActor):

    def on_start(self):
        self.state = False
        self.actors = []
        logging.info("GROUPED ACTOR")
        if self.props.get("Actor01", None) is not None:
            self.actors.append(self.props.get("Actor01"))
        if self.props.get("Actor02", None) is not None:
            self.actors.append(self.props.get("Actor02"))
        if self.props.get("Actor03", None) is not None:
            self.actors.append(self.props.get("Actor03"))
        if self.props.get("Actor04", None) is not None:
            self.actors.append(self.props.get("Actor04"))
        if self.props.get("Actor05", None) is not None:
            self.actors.append(self.props.get("Actor05"))
        if self.props.get("Actor06", None) is not None:
            self.actors.append(self.props.get("Actor06"))
        if self.props.get("Actor07", None) is not None:
            self.actors.append(self.props.get("Actor07"))
        if self.props.get("Actor08", None) is not None:
            self.actors.append(self.props.get("Actor08"))
        pass

    async def on(self, power=0):
        for actor in self.actors:
            await self.cbpi.actor.on(actor)
            self.state = True

    async def off(self):
        for actor in self.actors:
            await self.cbpi.actor.off(actor)
            self.state = False

    def get_state(self):
        return self.state
    
    async def run(self):
        pass


def setup(cbpi):
    cbpi.plugin.register("Grouped Actor", CustomActor)
    pass
