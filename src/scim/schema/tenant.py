# -*- coding: utf-8 -*-
from .core import Base
from . import attributes, types


class Tenant(Base):

    class Meta:
        schema = 'urn:scim:schemas:extension:tenant:1.0'

    display_name = attributes.Singular(types.String)
    """The name of the tenant, suitable for display to end-users."""

    preferred_language = attributes.Singular(types.String)
    """Indicates the tenant's preferred written or spoken language."""

    locale = attributes.Singular(types.String)
    """Used to indicate the tenant's default location for purposes of
    localizing items such as currency, date time format,
    numerical representations, etc."""

    timezone = attributes.Singular(types.String)
    """The tenant's time zone in the "Olson" timezone database
    format; e.g.,'America/Los_Angeles'."""

    active = attributes.Singular(types.Boolean)
    """A Boolean value indicating the tenant's administrative status."""

    entitlements = attributes.MultiValue()
    """A list of entitlements for the Tenant that represent
    a thing the Tenant has."""
