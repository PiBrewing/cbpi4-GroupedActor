
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

class GroupedActor(CBPiActor):

    # Custom property which can be configured by the user
    @action("Set Power", parameters=[Property.Number(label="Power", configurable=True,description="Power Setting [0-100]")])
    async def setpower(self,Power = 100 ,**kwargs):
        self.power=int(Power)
        if self.power < 0:
            self.power = 0
        if self.power > 100:
            self.power = 100           
        await self.set_power(self.power)   

    def on_start(self):
        self.state = False
        self.actors = []
        self.power = 100
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

    async def on(self, power=None):
        if power is not None:
            self.power = power

        for actor in self.actors:
            await self.cbpi.actor.on(actor,self.power)
            self.state = True
        await self.cbpi.actor.actor_update(self.id,power)

    async def off(self):
        for actor in self.actors:
            await self.cbpi.actor.off(actor)
            self.state = False

    def get_state(self):
        return self.state

    async def set_power(self, power):
        self.power = power
        for actor in self.actors:
            await self.cbpi.actor.set_power(actor,self.power)

        await self.cbpi.actor.actor_update(self.id,power)
        pass
    
    async def run(self):
        pass


def setup(cbpi):
    cbpi.plugin.register("Grouped Actor", GroupedActor)
    pass
