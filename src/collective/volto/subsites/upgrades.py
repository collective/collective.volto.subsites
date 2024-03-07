# -*- coding: utf-8 -*-
from collective.volto.subsites.setuphandlers import disable_searchable_type
from plone import api

DEFAULT_PROFILE = "profile-collective.volto.subsites:default"


def update_profile(context, profile, run_dependencies=True):
    context.runImportStepFromProfile(DEFAULT_PROFILE, profile, run_dependencies)


def update_types(context):
    update_profile(context, "typeinfo")


def update_rolemap(context):
    update_profile(context, "rolemap")


def update_registry(context):
    update_profile(context, "plone.app.registry", run_dependencies=False)


def update_catalog(context):
    update_profile(context, "catalog")


def update_controlpanel(context):
    update_profile(context, "controlpanel")


def to_1100(context):
    disable_searchable_type()


def to_1200(context):
    """"""
    # enable behavior
    portal_types = api.portal.get_tool(name="portal_types")
    behaviors = list(portal_types["Subsite"].behaviors)
    if "plone.versioning" not in behaviors:
        behaviors.append("plone.versioning")
    portal_types["Subsite"].behaviors = tuple(behaviors)

    # setup versioning in tools
    context.runImportStepFromProfile(DEFAULT_PROFILE, "plone-difftool")
    context.runImportStepFromProfile(DEFAULT_PROFILE, "repositorytool")
