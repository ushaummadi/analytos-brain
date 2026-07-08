permit (
    principal == User::"content-agent",
    action == Action::"read",
    resource in Product
);

permit (
    principal == User::"content-agent",
    action == Action::"read",
    resource in Feature
);

permit (
    principal == User::"content-agent",
    action == Action::"read",
    resource in ProofPoint
);

forbid (
    principal == User::"content-agent",
    action == Action::"read",
    resource in EmailThread
);

permit (
    principal == User::"gtm-agent",
    action == Action::"read",
    resource in Product
);

permit (
    principal == User::"gtm-agent",
    action == Action::"read",
    resource in Persona
);

permit (
    principal == User::"gtm-agent",
    action == Action::"read",
    resource in ICPSegment
);

permit (
    principal == User::"gtm-agent",
    action == Action::"read",
    resource in ProofPoint
);