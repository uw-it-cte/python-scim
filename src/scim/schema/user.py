# -*- coding: utf-8 -*-
from .core import Base
from . import attributes, types


class Username(attributes.Base):
    """The components of the User's real name.
    """

    formatted = attributes.Singular(types.String)
    """The full name, including all middle names, titles, and suffixes as
    appropriate, formatted for display (e.g. Ms. Barbara Jane Jensen, III.)."""

    family_name = attributes.Singular(types.String)
    """The family name of the User, or "Last Name" in
    most Western languages (e.g. Jensen given the full name Ms.
    Barbara Jane Jensen, III.)."""

    given_name = attributes.Singular(types.String)
    """The given name of the User, or "First Name" in most Western
    languages (e.g. Barbara given the full name
    Ms. Barbara Jane Jensen, III.)."""

    middle_name = attributes.Singular(types.String)
    """The middle name(s) of the User (e.g. Jane given the full
    name Ms. Barbara Jane Jensen, III.)."""

    honorific_prefix = attributes.Singular(types.String)
    """The honorific prefix(es) of the User, or "Title" in most
    Western languages (e.g. Ms. given the full name
    Ms. Barbara Jane Jensen, III.)."""

    honorific_suffix = attributes.Singular(types.String)
    """The honorific suffix(es) of the User, or "Suffix" in most
    Western languages (e.g. III. given the full name
    Ms. Barbara Jane Jensen, III.)."""


class User(Base):
    """SCIM provides a schema for representing Users (v1.1 § 6).
    """

    username = attributes.Singular(types.String, 'userName')
    """Unique identifier for the User, typically used by the user to directly
    authenticate to the service provider."""

    name = attributes.Complex(Username)
    """The components of the User's real name."""

    display_name = attributes.Singular(types.String)
    """The name of the User, suitable for display to end-users."""

    nick_name = attributes.Singular(types.String)
    """The casual way to address the user in real life, e.g. "Bob"
    or "Bobby" instead of "Robert"."""

    profile_url = attributes.Singular(types.String)
    """A fully qualified URL to a page representing the User's online profile.
    """

    title = attributes.Singular(types.String)
    """The user’s title, such as “Vice President.”"""

    user_type = attributes.Singular(types.String)
    """Used to identify the organization to user relationship.
    Typical values used might be "Contractor", "Employee",
    "Intern", "Temp", "External", and "Unknown" but any value may be used."""

    preferred_language = attributes.Singular(types.String)
    """Indicates the User's preferred written or spoken language."""

    locale = attributes.Singular(types.String)
    """Used to indicate the User's default location for purposes of
    localizing items such as currency, date time format,
    numerical representations, etc."""

    timezone = attributes.Singular(types.String)
    """The User's time zone in the "Olson" timezone database
    format; e.g.,'America/Los_Angeles'."""

    active = attributes.Singular(types.Boolean)
    """A Boolean value indicating the User's administrative status."""

    password = attributes.Singular(types.String)
    """The User's clear text password. This attribute is intended to be used
    as a means to specify an initial password when creating a new User or
    to reset an existing User's password.

    This value MUST never be returned by a Service Provider in any form."""

    emails = attributes.MultiValue()
    """E-mail addresses for the User."""

    phone_numbers = attributes.MultiValue()
    """Phone numbers for the User."""

    ims = attributes.MultiValue()
    """Instant messaging address for the User."""

    photos = attributes.MultiValue()
    """URL of a photo of the User."""

    # TODO: addresses

    # TODO: groups

    entitlements = attributes.MultiValue()
    """A list of entitlements for the User that represent a thing the User has.
    """

    roles = attributes.MultiValue()
    """A list of roles for the User that collectively represent who the
    User is."""

    # TODO: x509_certificates


class Manager(attributes.Base):

    id = attributes.Singular(types.String, 'managerId')
    """The id of the SCIM resource representing the User's manager."""

    uri = attributes.Singular(types.String, '$ref')
    """The URI of the SCIM resource representing the User's manager."""

    display_name = attributes.Singular(types.String)
    """The displayName of the User's manager."""


class EnterpriseUser(User):
    """
    Maps to the Enterprise User extension which defines attributes
    commonly used in representing users that belong to, or act on behalf
    of a business or enterprise (v2.0 § 7).
    """

    class Meta:
        schema = 'urn:scim:schemas:extension:enterprise:2.0:User'

    employee_number = attributes.Singular(types.String)
    """Numeric or alphanumeric identifier assigned to a
    person, typically based on order of hire or association with an
    organization."""

    cost_center = attributes.Singular(types.String)
    """Identifies the name of a cost center."""

    organization = attributes.Singular(types.String)
    """Identifies the name of an organization."""

    department = attributes.Singular(types.String)
    """Identifies the name of a department."""

    division = attributes.Singular(types.String)
    """Identifies the name of a division."""

    manager = attributes.Complex(Manager)
    """The User's manager.  A complex type that optionally allows
    Service Providers to represent organizational hierarchy by
    referencing the "id" attribute of another User."""
