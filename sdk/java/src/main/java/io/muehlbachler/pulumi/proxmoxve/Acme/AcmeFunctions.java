// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.Acme;

import com.pulumi.core.Output;
import com.pulumi.core.TypeShape;
import com.pulumi.deployment.Deployment;
import com.pulumi.deployment.InvokeOptions;
import com.pulumi.resources.InvokeArgs;
import io.muehlbachler.pulumi.proxmoxve.Acme.inputs.GetAccountArgs;
import io.muehlbachler.pulumi.proxmoxve.Acme.inputs.GetAccountPlainArgs;
import io.muehlbachler.pulumi.proxmoxve.Acme.outputs.GetAccountResult;
import io.muehlbachler.pulumi.proxmoxve.Acme.outputs.GetAccountsResult;
import io.muehlbachler.pulumi.proxmoxve.Utilities;
import java.util.concurrent.CompletableFuture;

public final class AcmeFunctions {
    /**
     * Retrieves information about a specific ACME account.
     * 
     * ## Example Usage
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.proxmoxve.Acme.AcmeFunctions;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var all = AcmeFunctions.getAccounts();
     * 
     *         final var example = "TODO: ForExpression";
     * 
     *         ctx.export("dataProxmoxVirtualEnvironmentAcmeAccount", example);
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetAccountResult> getAccount() {
        return getAccount(GetAccountArgs.Empty, InvokeOptions.Empty);
    }
    /**
     * Retrieves information about a specific ACME account.
     * 
     * ## Example Usage
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.proxmoxve.Acme.AcmeFunctions;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var all = AcmeFunctions.getAccounts();
     * 
     *         final var example = "TODO: ForExpression";
     * 
     *         ctx.export("dataProxmoxVirtualEnvironmentAcmeAccount", example);
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetAccountResult> getAccountPlain() {
        return getAccountPlain(GetAccountPlainArgs.Empty, InvokeOptions.Empty);
    }
    /**
     * Retrieves information about a specific ACME account.
     * 
     * ## Example Usage
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.proxmoxve.Acme.AcmeFunctions;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var all = AcmeFunctions.getAccounts();
     * 
     *         final var example = "TODO: ForExpression";
     * 
     *         ctx.export("dataProxmoxVirtualEnvironmentAcmeAccount", example);
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetAccountResult> getAccount(GetAccountArgs args) {
        return getAccount(args, InvokeOptions.Empty);
    }
    /**
     * Retrieves information about a specific ACME account.
     * 
     * ## Example Usage
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.proxmoxve.Acme.AcmeFunctions;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var all = AcmeFunctions.getAccounts();
     * 
     *         final var example = "TODO: ForExpression";
     * 
     *         ctx.export("dataProxmoxVirtualEnvironmentAcmeAccount", example);
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetAccountResult> getAccountPlain(GetAccountPlainArgs args) {
        return getAccountPlain(args, InvokeOptions.Empty);
    }
    /**
     * Retrieves information about a specific ACME account.
     * 
     * ## Example Usage
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.proxmoxve.Acme.AcmeFunctions;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var all = AcmeFunctions.getAccounts();
     * 
     *         final var example = "TODO: ForExpression";
     * 
     *         ctx.export("dataProxmoxVirtualEnvironmentAcmeAccount", example);
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetAccountResult> getAccount(GetAccountArgs args, InvokeOptions options) {
        return Deployment.getInstance().invoke("proxmoxve:Acme/getAccount:getAccount", TypeShape.of(GetAccountResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Retrieves information about a specific ACME account.
     * 
     * ## Example Usage
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.proxmoxve.Acme.AcmeFunctions;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var all = AcmeFunctions.getAccounts();
     * 
     *         final var example = "TODO: ForExpression";
     * 
     *         ctx.export("dataProxmoxVirtualEnvironmentAcmeAccount", example);
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetAccountResult> getAccountPlain(GetAccountPlainArgs args, InvokeOptions options) {
        return Deployment.getInstance().invokeAsync("proxmoxve:Acme/getAccount:getAccount", TypeShape.of(GetAccountResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Retrieves the list of ACME accounts.
     * 
     * ## Example Usage
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.proxmoxve.Acme.AcmeFunctions;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = AcmeFunctions.getAccounts();
     * 
     *         ctx.export("dataProxmoxVirtualEnvironmentAcmeAccounts", example.applyValue(getAccountsResult -> getAccountsResult.accounts()));
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetAccountsResult> getAccounts() {
        return getAccounts(InvokeArgs.Empty, InvokeOptions.Empty);
    }
    /**
     * Retrieves the list of ACME accounts.
     * 
     * ## Example Usage
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.proxmoxve.Acme.AcmeFunctions;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = AcmeFunctions.getAccounts();
     * 
     *         ctx.export("dataProxmoxVirtualEnvironmentAcmeAccounts", example.applyValue(getAccountsResult -> getAccountsResult.accounts()));
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetAccountsResult> getAccountsPlain() {
        return getAccountsPlain(InvokeArgs.Empty, InvokeOptions.Empty);
    }
    /**
     * Retrieves the list of ACME accounts.
     * 
     * ## Example Usage
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.proxmoxve.Acme.AcmeFunctions;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = AcmeFunctions.getAccounts();
     * 
     *         ctx.export("dataProxmoxVirtualEnvironmentAcmeAccounts", example.applyValue(getAccountsResult -> getAccountsResult.accounts()));
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetAccountsResult> getAccounts(InvokeArgs args) {
        return getAccounts(args, InvokeOptions.Empty);
    }
    /**
     * Retrieves the list of ACME accounts.
     * 
     * ## Example Usage
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.proxmoxve.Acme.AcmeFunctions;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = AcmeFunctions.getAccounts();
     * 
     *         ctx.export("dataProxmoxVirtualEnvironmentAcmeAccounts", example.applyValue(getAccountsResult -> getAccountsResult.accounts()));
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetAccountsResult> getAccountsPlain(InvokeArgs args) {
        return getAccountsPlain(args, InvokeOptions.Empty);
    }
    /**
     * Retrieves the list of ACME accounts.
     * 
     * ## Example Usage
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.proxmoxve.Acme.AcmeFunctions;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = AcmeFunctions.getAccounts();
     * 
     *         ctx.export("dataProxmoxVirtualEnvironmentAcmeAccounts", example.applyValue(getAccountsResult -> getAccountsResult.accounts()));
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetAccountsResult> getAccounts(InvokeArgs args, InvokeOptions options) {
        return Deployment.getInstance().invoke("proxmoxve:Acme/getAccounts:getAccounts", TypeShape.of(GetAccountsResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Retrieves the list of ACME accounts.
     * 
     * ## Example Usage
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.proxmoxve.Acme.AcmeFunctions;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = AcmeFunctions.getAccounts();
     * 
     *         ctx.export("dataProxmoxVirtualEnvironmentAcmeAccounts", example.applyValue(getAccountsResult -> getAccountsResult.accounts()));
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetAccountsResult> getAccountsPlain(InvokeArgs args, InvokeOptions options) {
        return Deployment.getInstance().invokeAsync("proxmoxve:Acme/getAccounts:getAccounts", TypeShape.of(GetAccountsResult.class), args, Utilities.withVersion(options));
    }
}